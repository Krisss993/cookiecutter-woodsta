const { merge } = require('webpack-merge');
const commonConfig = require('./common.config');

module.exports = merge(commonConfig, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    port: 3000,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*',
    },
    devMiddleware: {
      publicPath: '/static/webpack_bundles/',
    },
    proxy: [
      {
        context: ['/'],
        target: 'http://localhost:8000',
      },
    ],
    client: {
      overlay: {
        errors: true,
        warnings: false,
        runtimeErrors: true,
      },
    },
    // We need hot=false (Disable HMR) to set liveReload=true
    hot: false,
    liveReload: true,
  },
});
