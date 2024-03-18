import { IoFolderOpenOutline } from "react-icons/io5";
import { useState } from "react";

function AdminCard({ key, email, username, description, requestedAmount }) {
  return (
    <div>
      <div className="h-20"></div>
      <div className="flex justify-center items-center h-auto w-full p-3 top-20px">
        <div className="grid grid-rows-1 h-60 w-60 cursor-pointer items-center rounded-2xl bg-neutral-100 p-4 shadow-2xl transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-slate-200 md:w-[70%]">
          <div className="p-5">
            <h1 className="font-extrabold text-lg">{key}</h1>
            <h1 className="font-bold text-sm mb-2">{email}</h1>
            <h1 className="font-bold text-sm mb-2">{username}</h1>
            <p className="text-sm mb-4">{description}</p>
            <div className="grid grid-cols-2 gap-2">
              <div className="w-auto cursor-pointer items-center justify-center rounded-xl p-2 bg-green-400 hover:bg-green-500">
                <h1 className="text-white font-bold">{requestedAmount}</h1>
              </div>
            </div>
            <div className="flex justify-between mt-4">
              <button className="bg-lime-500 text-white rounded-2xl h-10 px-4 hover:bg-lime-600 focus:outline-none">Approve</button>
              <button className="bg-red-600 text-white rounded-2xl h-10 px-4 hover:bg-red-700 focus:outline-none">Decline</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AdminCard;
