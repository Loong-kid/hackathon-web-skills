---
name: web-build
description: Build functional HTML/CSS/JavaScript pages or small web apps in constrained environments using available project tooling. Use for implementation and local delivery; visual styling and browser verification can be supplied separately.
license: MIT
---

# Web Build

Deliver a working page within the requested scope and the environment's actual capabilities. This is a portable workflow, not the OpenAI Sites service.

## Establish the implementation boundary

Read the task, applicable project instructions, existing entry files, and dependency manifests first. Preserve an existing framework and build pipeline. For a new static page or browser-local tool, prefer HTML, CSS, and JavaScript without a build step. Use a backend only when the requested behavior requires one and the environment supports it.

Check the provided runtime and preview tools before adding dependencies. Respect the sandbox's allowed download sources. If only GitHub downloads are permitted, do not pull packages, fonts, scripts, or images from npm, PyPI, CDNs, or image services. Existing installed dependencies remain usable. Prefer system fonts and local assets. A skill download does not install a browser, grant a service connection, or supply an API key.

Resolve a missing product decision only when it blocks implementation. For routine choices, state a reasonable assumption and continue. Derive a short acceptance list from the requested behavior, including the main interaction and the expected submission format. Keep any design plan brief enough to leave time for building.

## Build a complete interaction

- Implement the primary user journey before secondary polish. A search should change results; filters should filter; a dialog should open, close, and return focus; a form should validate and show a meaningful outcome.
- Give data-driven views useful empty and error states. Use loading states when work is actually asynchronous. Mark demonstration data as demonstration data; do not invent testimonials or performance claims.
- Use semantic controls, associated form labels, visible keyboard focus, and responsive layout. Preserve the user's specified brand and visual direction. When a design skill is selected, use it for visual choices without duplicating two full design workflows.
- Keep asset paths relative to the deliverable and package consumed assets with it. Avoid runtime network dependencies for a static submission. Choose a system font fallback that works when external font hosts are blocked.
- Use browser storage only for appropriate non-secret, browser-local state. Explain when data is local to one browser. Do not simulate real authentication, payments, or server persistence as if they were connected.
- If the user requests one HTML file, inline the required CSS, JavaScript, and suitable assets rather than introducing a framework or extra required files.

## Run and hand off

Use the project's existing preview command. For a buildless directory with Python available, a local static server such as `python -m http.server 8000 --bind 127.0.0.1` can serve it; adapt host and port to the environment's preview interface. Stop only processes you started when they are no longer needed.

Run the relevant available checks. Exercise the main behavior and inspect the rendered page if a browser is available. If it is unavailable, report exactly which static or runtime checks were possible and which visual checks remain unverified. Never claim a screenshot or browser interaction that did not happen.

Return the entry file or preview location, launch instructions, checks performed, and material limitations. Produce the requested local artifact or submission package. Use a hosting provider only when the user asks for deployment and the required connection is available.
