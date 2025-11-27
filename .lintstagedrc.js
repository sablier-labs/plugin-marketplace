/**
 * @type {import("lint-staged").Configuration}
 */
module.exports = {
  "*.md": "mdformat",
  "*.{json,jsonc,yaml,yml}": "nlx prettier --write",
};
