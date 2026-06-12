import{a as p,j as f}from"./react-vendor-dPJNWl6a.js";function u(){return p.useEffect(()=>{const v=window.matchMedia("(prefers-reduced-motion: reduce)").matches,h=Array.from(document.querySelectorAll(".calchive-static-motion")),n=[],s=[];return h.forEach(i=>{i.classList.add("calchive-motion-ready");const d=["h1","h2","h3","p","article","aside","form",".bg-card","[data-scroll-reveal]"].join(","),r=Array.from(new Set(Array.from(i.querySelectorAll(d)))).filter(e=>{if(e.closest("[data-no-scroll-motion]"))return!1;const a=e.matches("h3, p"),o=!!e.closest(".bg-card, article, aside, form");return!(a&&o)});if(r.forEach((e,a)=>{e.classList.add("calchive-reveal"),e.style.setProperty("--reveal-delay",`${Math.min(a%7*38,228)}ms`),e.matches(".bg-card, .rounded-2xl, .rounded-3xl, article, aside")?e.classList.add("calchive-reveal-pop"):a%5===1?e.classList.add("calchive-reveal-left"):a%5===2&&e.classList.add("calchive-reveal-right")}),v||!("IntersectionObserver"in window)){r.forEach(e=>e.classList.add("calchive-reveal-in"));return}let t=!1;const m=()=>{t=!1;const e=window.innerHeight*.92;r.forEach(a=>{if(a.classList.contains("calchive-reveal-in"))return;const o=a.getBoundingClientRect();o.top<e&&o.bottom>0&&a.classList.add("calchive-reveal-in")})},c=()=>{t||(t=!0,window.requestAnimationFrame(m))},l=new IntersectionObserver(e=>{e.forEach(a=>{a.isIntersecting&&(a.target.classList.add("calchive-reveal-in"),l.unobserve(a.target))})},{rootMargin:"0px 0px -10% 0px",threshold:.08});r.forEach(e=>l.observe(e)),n.push(l),c(),window.addEventListener("scroll",c,{passive:!0}),window.addEventListener("resize",c,{passive:!0}),s.push(()=>{window.removeEventListener("scroll",c),window.removeEventListener("resize",c)})}),()=>{n.forEach(i=>i.disconnect()),s.forEach(i=>i())}},[]),f.jsx("style",{children:`
      .calchive-static-motion {
        animation: calchivePageRise 380ms cubic-bezier(.22,1,.36,1) both;
      }

      .calchive-motion-ready.calchive-reveal,
      .calchive-motion-ready .calchive-reveal {
        opacity: 0;
        transform: translate3d(0, 22px, 0) scale(.992);
        transition:
          opacity 560ms cubic-bezier(.22,1,.36,1),
          transform 560ms cubic-bezier(.22,1,.36,1),
          box-shadow 220ms ease,
          border-color 220ms ease,
          background-color 220ms ease;
        transition-delay: var(--reveal-delay, 0ms);
        will-change: opacity, transform;
      }

      .calchive-motion-ready.calchive-reveal-left,
      .calchive-motion-ready .calchive-reveal-left {
        transform: translate3d(-18px, 18px, 0) scale(.992);
      }

      .calchive-motion-ready.calchive-reveal-right,
      .calchive-motion-ready .calchive-reveal-right {
        transform: translate3d(18px, 18px, 0) scale(.992);
      }

      .calchive-motion-ready.calchive-reveal-pop,
      .calchive-motion-ready .calchive-reveal-pop {
        transform: translate3d(0, 20px, 0) scale(.972);
      }

      .calchive-motion-ready.calchive-reveal-in,
      .calchive-motion-ready .calchive-reveal-in,
      .calchive-motion-ready.calchive-reveal-in.calchive-reveal-left,
      .calchive-motion-ready .calchive-reveal-in.calchive-reveal-left,
      .calchive-motion-ready.calchive-reveal-in.calchive-reveal-right,
      .calchive-motion-ready .calchive-reveal-in.calchive-reveal-right,
      .calchive-motion-ready.calchive-reveal-in.calchive-reveal-pop,
      .calchive-motion-ready .calchive-reveal-in.calchive-reveal-pop {
        opacity: 1;
        transform: translate3d(0, 0, 0) scale(1);
      }

      .calchive-static-motion :where(a, button, .group) {
        transition-property: transform, box-shadow, border-color, background-color, color, opacity;
        transition-duration: 180ms;
        transition-timing-function: cubic-bezier(.22,1,.36,1);
      }

      .calchive-static-motion :where(a:hover, button:hover, .group:hover) {
        transform: translateY(-1px);
      }

      @keyframes calchivePageRise {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
      }

      @media (max-width: 640px) {
        .calchive-static-motion {
          animation-duration: 240ms;
        }

        .calchive-motion-ready.calchive-reveal,
        .calchive-motion-ready .calchive-reveal,
        .calchive-motion-ready.calchive-reveal-left,
        .calchive-motion-ready .calchive-reveal-left,
        .calchive-motion-ready.calchive-reveal-right,
        .calchive-motion-ready .calchive-reveal-right,
        .calchive-motion-ready.calchive-reveal-pop,
        .calchive-motion-ready .calchive-reveal-pop {
          transform: translate3d(0, 14px, 0) scale(.988);
          transition-duration: 360ms;
          transition-delay: min(var(--reveal-delay, 0ms), 120ms);
        }

        .calchive-static-motion :where(a:hover, button:hover, .group:hover) {
          transform: none;
        }

      }

      @media (prefers-reduced-motion: reduce) {
        .calchive-static-motion,
        .calchive-motion-ready.calchive-reveal,
        .calchive-motion-ready .calchive-reveal,
        .calchive-motion-ready.calchive-reveal-left,
        .calchive-motion-ready .calchive-reveal-left,
        .calchive-motion-ready.calchive-reveal-right,
        .calchive-motion-ready .calchive-reveal-right,
        .calchive-motion-ready.calchive-reveal-pop,
        .calchive-motion-ready .calchive-reveal-pop {
          animation: none !important;
          transition: none !important;
          opacity: 1 !important;
          transform: none !important;
          will-change: auto !important;
        }
      }
    `})}export{u as S};
//# sourceMappingURL=StaticPageMotion-Cnl9TtTi.js.map
