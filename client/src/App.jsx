import "./App.css";
import Home from "./pages/Home/Home";
import {
    BrowserRouter,
    Routes,
    Route,
    RouterProvider,
    createBrowserRouter,
} from "react-router-dom";
import ErrorPage from "./ErrorPage";
import SignUp from "./pages/SignUp/SignUp";
import Navbar from "./components/navbar/Navbar";
import SignIn from "./pages/SignIn/SignIn.jsx";
import LandingPage from "./pages/Landing/LandingPage.jsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Home />,
        errorElement: <ErrorPage />,
    },
]);

function App() {
    return (
        <>
            <BrowserRouter>
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />}></Route>
                    <Route path="/signup" element={<SignUp />}></Route>
                    <Route path="/signin" element={<SignIn />}></Route>
                    <Route path="/landingpage/v1" element={< LandingPage />}></Route>
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default App;
