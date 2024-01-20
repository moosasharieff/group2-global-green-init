import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

function SignIn() {
    const navigate = useNavigate();
    const [localToken, setLocalToken] = useState(false);
    const [userEmail, setUserEmail] = useState("");
    const [userPassword, setUserPassword] = useState("");

    const handleRegisteration = async (e) => {
        e.preventDefault();
        await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
            username: userEmail,
            password: userPassword
        }).then((res ) => {
            console.log(res.data.token);
            localStorage.setItem('loginAuthToken', res.data.token)
            if(localStorage.getItem('loginAuthToken')){
                setLocalToken(true);
                setTimeout(() => {
                    setLocalToken(false);
                    navigate('/landingpage/v1')
                }, 2000)
            }

        }).catch((e)=>{
            console.error(e);
        })
    };

    return (
        <div className="fixed h-screen w-full bg-lime-50">
            <div className="h-2/4 w-100 p-20 font-extrabold text-[240px] bg-green-500 ">Nausicca&apos;s.</div>
            <div className="h-2/4 w-100 px-[700px] font-extrabold text-[240px] bg-lime-50">Green.</div>
            {/* <div className="blur-md"> */}
            <form
                className="absolute bg-opacity-80 hover:drop-shadow-2xl hover:bg-green-300 backdrop-filter h-3/4 w-auto p-6 bg-green-200 top-[10%] left-[32%] rounded-lg grid grid-flow-row gap-0 items-center"
                onSubmit={handleRegisteration}
                >
                <h1 className="text-green-700 text-4xl font-bold pt-4">Nausicca&apos;s</h1>
                <div className="grid grid-flow-row gap-4 w-[400px]">
                    <label htmlFor="email">
                        <input
                            className="border-slate-200 placeholder:indent-4 placeholder-slate-400 outline-none h-12 w-full rounded-md "
                            type="text"
                            value={userEmail}
                            placeholder="Email"
                            onChange={(e) => setUserEmail(e.target.value)}
                        />
                    </label>
                    <label htmlFor="username">
                        <input
                            className="border-slate-200 placeholder:indent-4 placeholder-slate-400 outline-none h-12 w-full rounded-md "
                            type="password"
                            value={userPassword}
                            placeholder="Password"
                            onChange={(e) => setUserPassword(e.target.value)}
                        />
                    </label>
                </div>
                <button
                    className="rounded-lg text-green-700 h-12 hover:bg-green-400 hover:text-white"
                    type="submit"
                    >
                    Sign In
                </button>
                {localToken && <>loading.......</>}
                <p>New here? <Link to="/signup">Sign in</Link></p>
            </form>
            {/* </div> */}
        </div>
        );
}

export default SignIn;
