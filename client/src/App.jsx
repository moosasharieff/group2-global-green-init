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
  const base_uri = `${process.env.REACT_APP_URL}/roles`;
  const userRoles = user && user[base_uri];
  console.log(userRoles)

  const getUserRoles = async () => {
    var options = {
      method: 'POST',
      url: process.env.REACT_APP_TOKEN_URI,
      headers: { 'content-type': 'application/x-www-form-urlencoded' },
      data: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: process.env.REACT_APP_ROLES_CLIENT_ID,
        client_secret: process.env.REACT_APP_CLIENT_SECRET,
        audience: process.env.REACT_APP_ROLES_AUDIENCE
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
              {console.log(user)}
              {user && user[base_uri]?.includes('superuser') ? (
                <Route
                  path="/"
                  element={<Navigate to="/admin" />}
                />
              ) : (
                <Route path="/" element={<LandingPage />} />
              )}
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
