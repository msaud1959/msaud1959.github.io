/* Mohammad Saud — portfolio WebGL background.
   A "neural core": wireframe icosahedron + inner core, orbital rings,
   particle field and floating satellites. Reacts to scroll and mouse.
   Three.js loaded from CDN via importmap. Degrades silently if WebGL
   is unavailable; disabled for reduced-motion users. */

import * as THREE from "three";

(function () {
  "use strict";

  const canvas = document.getElementById("bg3d");
  if (!canvas) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    canvas.remove();
    return;
  }

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  } catch (e) {
    canvas.remove();
    return;
  }

  const isMobile = window.matchMedia("(max-width: 720px)").matches;
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, isMobile ? 1.5 : 2));
  renderer.setSize(window.innerWidth, window.innerHeight);

  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(0x06080f, 0.018);

  const camera = new THREE.PerspectiveCamera(55, window.innerWidth / window.innerHeight, 0.1, 120);
  camera.position.set(0, 0, 26);

  const CYAN = 0x22d3ee, VIOLET = 0x8b5cf6, PINK = 0xf472b6;

  /* ---- the core group (sits right of centre on desktop) ---- */
  const core = new THREE.Group();
  scene.add(core);

  const outerShell = new THREE.LineSegments(
    new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(7, 1)),
    new THREE.LineBasicMaterial({ color: CYAN, transparent: true, opacity: 0.34 })
  );
  core.add(outerShell);

  const innerCore = new THREE.LineSegments(
    new THREE.WireframeGeometry(new THREE.IcosahedronGeometry(3.4, 0)),
    new THREE.LineBasicMaterial({ color: VIOLET, transparent: true, opacity: 0.65 })
  );
  core.add(innerCore);

  /* node points on the shell vertices — "neural" look */
  const shellPts = new THREE.Points(
    new THREE.IcosahedronGeometry(7, 1),
    new THREE.PointsMaterial({ color: CYAN, size: 0.22, transparent: true, opacity: 0.9, sizeAttenuation: true })
  );
  core.add(shellPts);

  /* orbital rings */
  function ring(radius, color, opacity) {
    const r = new THREE.Mesh(
      new THREE.TorusGeometry(radius, 0.035, 8, 140),
      new THREE.MeshBasicMaterial({ color: color, transparent: true, opacity: opacity })
    );
    core.add(r);
    return r;
  }
  const ring1 = ring(10.2, VIOLET, 0.45);
  const ring2 = ring(12.6, PINK, 0.28);
  ring1.rotation.x = 1.15;
  ring2.rotation.x = 1.95;
  ring2.rotation.y = 0.4;

  /* ---- particle field (deep background) ---- */
  const COUNT = isMobile ? 350 : 850;
  const pos = new Float32Array(COUNT * 3);
  const col = new Float32Array(COUNT * 3);
  const cA = new THREE.Color(CYAN), cB = new THREE.Color(VIOLET), cC = new THREE.Color(PINK);
  for (let i = 0; i < COUNT; i++) {
    const r = 16 + Math.random() * 38;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    pos[i * 3] = r * Math.sin(phi) * Math.cos(theta);
    pos[i * 3 + 1] = r * Math.sin(phi) * Math.sin(theta) * 0.7;
    pos[i * 3 + 2] = r * Math.cos(phi) - 10;
    const t = Math.random();
    const c = t < 0.5 ? cA.clone().lerp(cB, t * 2) : cB.clone().lerp(cC, (t - 0.5) * 2);
    col[i * 3] = c.r; col[i * 3 + 1] = c.g; col[i * 3 + 2] = c.b;
  }
  const pGeo = new THREE.BufferGeometry();
  pGeo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  pGeo.setAttribute("color", new THREE.BufferAttribute(col, 3));
  const particles = new THREE.Points(pGeo, new THREE.PointsMaterial({
    size: 0.14, vertexColors: true, transparent: true, opacity: 0.8,
    sizeAttenuation: true, depthWrite: false
  }));
  scene.add(particles);

  /* ---- floating satellites (octahedra drifting at depths) ---- */
  const sats = new THREE.Group();
  scene.add(sats);
  const satGeo = new THREE.OctahedronGeometry(0.9, 0);
  const satColors = [CYAN, VIOLET, PINK];
  for (let i = 0; i < (isMobile ? 4 : 8); i++) {
    const m = new THREE.LineSegments(
      new THREE.WireframeGeometry(satGeo),
      new THREE.LineBasicMaterial({ color: satColors[i % 3], transparent: true, opacity: 0.5 })
    );
    m.position.set((Math.random() - 0.5) * 44, (Math.random() - 0.5) * 26, -6 - Math.random() * 22);
    m.userData.spin = 0.2 + Math.random() * 0.5;
    m.userData.bob = Math.random() * Math.PI * 2;
    sats.add(m);
  }

  /* ---- layout: keep the core clear of the text column ---- */
  function layout() {
    const w = window.innerWidth, h = window.innerHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
    if (w > 980) { core.position.set(9, 0, -4); core.scale.setScalar(1); }
    else { core.position.set(0, 5, -10); core.scale.setScalar(0.75); }
  }
  layout();
  window.addEventListener("resize", layout);

  /* ---- input: scroll + mouse drive the scene ---- */
  let scrollT = 0, mouseX = 0, mouseY = 0;
  window.addEventListener("scroll", function () {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    scrollT = max > 0 ? window.scrollY / max : 0;
  }, { passive: true });
  window.addEventListener("mousemove", function (e) {
    mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
    mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
  }, { passive: true });

  /* ---- animate ---- */
  const clock = new THREE.Clock();
  let running = true;
  document.addEventListener("visibilitychange", function () {
    running = !document.hidden;
    if (running) { clock.getDelta(); animate(); }
  });

  function animate() {
    if (!running) return;
    requestAnimationFrame(animate);
    const t = clock.getElapsedTime();

    /* core: idle spin + scroll-driven revolution + mouse parallax */
    core.rotation.y = t * 0.08 + scrollT * Math.PI * 2.2 + mouseX * 0.12;
    core.rotation.x = Math.sin(t * 0.11) * 0.12 + scrollT * 0.9 + mouseY * 0.08;
    innerCore.rotation.y = -t * 0.3;
    innerCore.rotation.z = t * 0.18;
    ring1.rotation.z = t * 0.16;
    ring2.rotation.z = -t * 0.12;

    /* breathing core */
    const pulse = 1 + Math.sin(t * 1.4) * 0.045;
    innerCore.scale.setScalar(pulse);

    /* particles: slow drift + scroll rotation */
    particles.rotation.y = t * 0.014 + scrollT * 0.9;
    particles.position.y = scrollT * 7 - 2;

    /* satellites: tumble + bob, drift upward as you scroll */
    sats.children.forEach(function (m, i) {
      m.rotation.x = t * m.userData.spin;
      m.rotation.y = t * m.userData.spin * 0.7;
      m.position.y += Math.sin(t * 0.6 + m.userData.bob) * 0.003;
    });
    sats.position.y = scrollT * 11;

    /* camera: gentle mouse sway */
    camera.position.x += (mouseX * 1.4 - camera.position.x) * 0.03;
    camera.position.y += (-mouseY * 1.0 - camera.position.y) * 0.03;
    camera.lookAt(0, 0, -4);

    renderer.render(scene, camera);
  }
  animate();
})();
