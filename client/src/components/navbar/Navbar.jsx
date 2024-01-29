import Logo from "../../assets/plant.svg";
import { useAuth0 } from "@auth0/auth0-react";

function Navbar() {
    const { logout } = useAuth0();
    const handleLogout = () => {
        console.log("user logout");
    };

    return (
        <div className="w-full flex h-16 text-lg bg-lime-50 justify-center">
            <ul className="m-x-10 w-[80%] flex items-center justify-center">
                <li key={1} className="h-12 w-12">
                    {" "}
                    <img src={Logo} alt="logo" />
                </li>
                <li key={2} className="ml-auto">
                    <div
                        className="h-12 w-12 bg-black rounded-full cursor-pointer"
                        onClick={() => logout({ returnTo: window.location.origin })}
                    ></div>
                </li>
            </ul>
        </div>
    );
}

export default Navbar;
