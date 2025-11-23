/**
 * API Configuration for Case Detector
 * This file determines which backend URL to use based on the environment
 */

// Detect environment and set API base URL
const API_CONFIG = (function() {
    const hostname = window.location.hostname;
    
    // Production: Vercel frontend connecting to Render backend
    if (hostname === 'case-detector.vercel.app') {
        return {
            API_BASE_URL: 'https://case-detector.onrender.com',
            environment: 'production'
        };
    }
    
    // Development: localhost
    if (hostname === 'localhost' || hostname === '127.0.0.1') {
        return {
            API_BASE_URL: window.location.origin,
            environment: 'development'
        };
    }
    
    // Default: use same origin
    return {
        API_BASE_URL: window.location.origin,
        environment: 'unknown'
    };
})();

// Export configuration
window.API_BASE_URL = API_CONFIG.API_BASE_URL;
window.API_ENVIRONMENT = API_CONFIG.environment;

// Configure axios if available
if (typeof axios !== 'undefined') {
    axios.defaults.baseURL = API_CONFIG.API_BASE_URL;
    axios.defaults.withCredentials = true;
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
}

console.log('🔧 API Configuration:', API_CONFIG);
