import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import LandingPage from "./pages/Landing/LandingPage";
import { useAuth0 } from "@auth0/auth0-react";
import LogIn from "./pages/SignIn/LogIn";
import SignIn from "./pages/SignIn/SignIn";

function App() {
    const { isAuthenticated } = useAuth0();
    return (
        <BrowserRouter>
            {isAuthenticated ? (
                <Routes>
                    <Route path="/" element={<LandingPage />} />
                </Routes>
            ) : (
                <SignIn />
            )}
        </BrowserRouter>
    );
}

export default App;