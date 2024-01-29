import Logo from "../../assets/plant.svg";
import { useAuth0 } from "@auth0/auth0-react";

function SignIn() {
    const { loginWithRedirect } = useAuth0();  


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
                            <button
                                className="rounded-lg text-green-700 h-12 hover:bg-green-400 hover:text-white"
                                type="submit"
                                onClick={() => loginWithRedirect()}
                            >
                                Sign In
                            </button>
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
