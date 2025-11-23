// Central API configuration for frontend
// For Vercel deployment, use the Render backend URL
// For local Django development, use empty string or localhost
const API_BASE_URL = "https://case-detector.onrender.com";

// Configure axios to use the backend URL
if (typeof axios !== 'undefined') {
    axios.defaults.baseURL = API_BASE_URL;
    console.log('Axios configured with base URL:', API_BASE_URL);
}
