// Serve the generated artifact; Jekyll and Turtle remain the build authorities.
export default {
  root: '_site',
  publicDir: false,
  appType: 'mpa',
  server: {
    host: '0.0.0.0',
    allowedHosts: ['terminal.local'],
    fs: {strict: true, allow: ['_site']},
  },
};
