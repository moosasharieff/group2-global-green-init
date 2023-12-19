import React from "react";
import { Link } from "react-router-dom";

const navItems = [
  { id: 0, menu: "Logo", to: "/" },
  { id: 1, menu: "Home", to: "/" },
  { id: 2, menu: "Contact", to: "/" },
  { id: 3, menu: "Sign Up", to: "/signup" },
  { id: 4, menu: "Sign In", to: "/" },
];

function Navbar() {
  return (
    <div className="flex flex-col sm:flex-row h-16 font-bold text-lg bg-lime-50">
      <ul className="flex sm:space-x-8 items-center justify-around w-full">
        <li className="cursor-pointer">{navItems[0].menu}</li>
        <div className="flex w-full sm:w-96 justify-between">
          {navItems.slice(1).map(function (items) {
            return (
              <li
                className="cursor-pointer p-1 hover:drop-shadow-2xl hover:text-green-400 hover:underline underline-offset-8 hover:rounded-lg"
                key={items.id}
              >
                <Link to={items.to}>{items.menu}</Link>
              </li>
            );
          })}
        </div>
      </ul>
    </div>
  );
}

export default Navbar;
