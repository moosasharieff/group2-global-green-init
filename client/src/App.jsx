import { useState, useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import LandingPage from "./pages/Landing/LandingPage.jsx";
import ClipLoader from "react-spinners/ClipLoader";
import Home from "./pages/Home/Home.jsx";
import AdminPage from "./pages/Admin/AdminPage";
import axios from "axios";

function App() {
  const { isAuthenticated, user, getAccessTokenSilently } = useAuth0();
  const [loading, setLoading] = useState(true);
  const userRoles = user && user['https://shav-xmdaoxl28shfvujc.eu.auth0.com/roles'];

  const getUserRoles = async () => {
    var options = {
      method: 'POST',
      url: 'https://shav-xmdaoxl28shfvujc.eu.auth0.com/oauth/token',
      headers: {'content-type': 'application/x-www-form-urlencoded'},
      data: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: 'EiDSGIyJ2oYN1kd6Xs3WPmbzmzzww5Dr',
        client_secret: '_9gmPdHEoqRGHVDFMzne5Dvfm37WrRHGFQnjnoqyj5PPtLq3be7BRWkd3bkYGPaQ',
        audience: 'https://shav-xmdaoxl28shfvujc.eu.auth0.com/api/v2/'
      })
    };
    
    axios.request(options).then(function (response) {
      console.log(response.data);
    }).catch(function (error) {
      console.error(error);
    });
  };

  useEffect(() => {
    const timeout = setTimeout(() => {
      setLoading(false);
    }, 2000);
    return () => clearTimeout(timeout);
  }, []);

  if (loading) {
    return (
      <div className="flex h-screen items-center justify-center">
        <div className="text-center">
          <ClipLoader size={150} color={"#26fa0f"} loading={loading} />
        </div>
      </div>
    );
  }

  return (
    <div className="bg-neutral-50">
      <BrowserRouter>
        <Routes>
          {isAuthenticated ? (
            <>
            {/* for user roles change the url based on your namespace (domain name) */}
              {user && user['http://localhost:5173//roles']?.includes('superuser') ? ( 
                <Route
                  path="/"
                  element={<Navigate to="/admin" />}
                />
              ) : (
                <Route path="/" element={<LandingPage />} />
              )}
              {/* Regular user routes */}
              <Route path="/admin" element={<AdminPage />} />
            </>
          ) : (
            <Route path="/" element={<Home />} />
          )}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
