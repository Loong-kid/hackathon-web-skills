---
name: web-check
description: Verify a web page's main interactions, responsive layout, accessibility basics, and delivery files using tools already available in the sandbox. Use after building or when diagnosing a concrete UI defect.
license: MIT
---

# Web Check

Test the requested behavior against the actual deliverable. Choose checks proportional to the change and time available; avoid setting up a testing framework for a small static edit.

## Choose an available verification path

Inspect the existing package scripts, installed browser automation, and preview interface. Reuse available tools rather than downloading a new browser or test dependency. Follow the sandbox's network restrictions. If no browser is available, perform the applicable source, asset, syntax, and HTTP checks and state that rendered layout and browser interactions were not verified.

## Check the user journey

Derive scenarios from the task's acceptance criteria. Exercise the normal path and the most relevant boundary: empty input, no results, invalid form data, repeated actions, or a refreshed page. Confirm controls change the intended state and displayed output. Check links and submission results; a visible success toast alone does not establish that a backend action occurred.

For asynchronous work, inspect loading, failure, and retry behavior when it exists. For browser-local persistence, refresh and confirm the intended state survives. Check that sample data is identified and that unavailable integrations are not presented as connected.

## Inspect the rendered page when possible

Use at least one narrow phone width and the intended desktop width, plus any widths specified by the task. Inspect overflow, clipped text, image sizing, navigation, forms, and content order. Test keyboard traversal, visible focus, form labels, dialog dismissal, and focus return. Check reduced-motion behavior if the page includes significant animation.

Review browser console errors and failed asset requests. If the environment supports screenshots, inspect actual screenshots rather than inferring layout from CSS. Avoid hiding horizontal overflow to conceal a broken layout.

## Check the submitted files

Confirm the entry file exists, referenced local assets are included, and a clean launch or the existing production build works. Use syntax tools where available; for ES modules, use the project's configured parser or a browser rather than incorrectly treating module source as a classic script. Check relative paths against the submission root and identify any network dependency that would break the delivered page.

Fix material defects within the authorized scope, then repeat only the checks affected by the fix. Report what ran, what passed, and what remains unverified. Distinguish real results from source inspection and proposed tests.
