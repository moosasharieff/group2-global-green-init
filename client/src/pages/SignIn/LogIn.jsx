import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import Logo from "../../assets/plant.svg";
import { useAuth0 } from "@auth0/auth0-react";

function SignIn() {
    // const navigate = useNavigate();
    // const [localToken, setLocalToken] = useState(false);
    // const [userEmail, setUserEmail] = useState("");
    // const [userPassword, setUserPassword] = useState("");

    // const handleRegisteration = async (e) => {
    //     e.preventDefault();
    //     await axios
    //         .post("http://127.0.0.1:8000/api/accounts/login/", {
    //             username: userEmail,
    //             password: userPassword,
    //         })
    //         .then((res) => {
    //             console.log(res.data);
    //             console.log(res.data.token);
    //             localStorage.setItem("loginAuthToken", res.data.token);
    //             if (localStorage.getItem("loginAuthToken")) {
    //                 // localStorage.removeItem("loginAuthToken");
    //                 setLocalToken(true);
    //                 setTimeout(() => {
    //                     setLocalToken(false);
    //                     navigate("/landingpage/v1");
    //                 }, 2000);
    //             }
    //         })
    //         .catch((e) => {
    //             console.error(e);
    //         });
    // };

    return (
        <div className="grid grid-cols-2">
            <div className="flex items-center justify-center h-screen w-full p-20 bg-lime-50">
                <div className=" bg-opacity-80 hover:drop-shadow-2xl h-3/4 w-3/4 rounded-xl hover:bg-green-300 backdrop-filter p-6 bg-green-200 grid grid-cols-1 gap-10 items-center justify-center ">
                    {/* name of the product */}
                    {/* form
                            user name 
                            pass
                        button
                        sign up 
                    */}
                    <div className="h-full grid grid-cols-1">
                        <div className="grid grid-cols-1 place-items-center">
                            <img className="h-14 w-14" src={Logo} alt="" />
                            <h1 className="text-5xl text-green-700 font-bold">
                                Nausicca&apos;s
                            </h1>
                        </div>
                        <form
                            onSubmit={handleRegisteration}
                            className="grid grid-cols-1 items-center justify-center"
                        >
                            <label htmlFor="email-input">
                                <input
                                    className="border-slate-200 placeholder:indent-4 placeholder-slate-400 outline-none h-12 w-full rounded-md "
                                    id="email-input"
                                    type="text"
                                    value={userEmail}
                                    placeholder="Email"
                                    onChange={(e) =>
                                        setUserEmail(e.target.value)
                                    }
                                />
                            </label>
                            <label htmlFor="pass-input">
                                <input
                                    className="border-slate-200 placeholder:indent-4 placeholder-slate-400 outline-none h-12 w-full rounded-md "
                                    id="pass-input"
                                    type="password"
                                    value={userPassword}
                                    placeholder="Password"
                                    onChange={(e) =>
                                        setUserPassword(e.target.value)
                                    }
                                />
                            </label>
                            <button
                                className="rounded-lg text-green-700 h-12 hover:bg-green-400 hover:text-white"
                                type="submit"
                                onClick={() => loginWithRedirect()}
                            >
                                Sign In
                            </button>
                            {localToken && <>loading.......</>}
                            <p>
                                New here? <Link to="/signup">Sign in</Link>
                            </p>
                        </form>
                    </div>
                </div>
            </div>
            <div className="h-screen bg-green-500 flex items-center justify-center">
                {/* Green. */}
                {/* create a Carousels of images <name> */}
                {/* <Carousel /> */}
            </div>
        </div>
    );
}

export default SignIn;
