import { IoFolderOpenOutline } from "react-icons/io5";
import { useState } from "react";
import axios from "axios";

function AdminCard({ key, granterName, email, username, description, requestedAmount }) {
  console.log(`granter name -ijakjndkabdiabi : ${granterName}`)
  const handleApprove = async () => {
    try {
      const userData = {
        email,
        granterName,
        grantStatus: true,
      };
      console.log(`userdata -----> ${userData}`);
      const api_url = `${process.env.REACT_APP_API_BASE_URL}api/admin-decision`;
      console.log(api_url);
      const response = await axios.post(api_url, userData);

      console.log("Response from server: --------", response.data);

      alert("Your grant application has been submitted!");
    } catch (error) {
      console.error("Error making Axios POST request:", error);
    }
  };

  return (
    <div>
      <div className="flex justify-center items-center h-auto w-full py-20 top-20px">
        <div className="grid grid-rows-1 h-60 w-60 cursor-pointer items-center rounded-2xl bg-neutral-100 p-6 shadow-2xl transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-110 hover:bg-slate-200 md:w-[70%]">
          <div className="p-5">
            <h1 className="font-extrabold text-lg">{key}</h1>
            <h1 className="font-bold text-sm mb-2">{email}</h1>
            <h1 className="font-bold text-sm mb-2">{username}</h1>
            <p className="text-sm mb-4 w-auto h-auto">{description}</p>
            <div className="grid grid-cols-2 gap-2 items-center">
              <div className="w-32 cursor-pointer items-center justify-center rounded-xl p-2 bg-green-400 hover:bg-green-500">
                <h1 className="text-white font-bold">€{requestedAmount}</h1>
                <h1>Requested for {granterName}</h1>
              </div>
              
            </div>
            <div className="flex justify-between mt-4">
              <button
                onClick={handleApprove}
                className="bg-lime-500 text-white rounded-2xl h-10 px-4 hover:bg-lime-600 focus:outline-none"
              >
                Approve
              </button>
              <button className="bg-red-600 text-white rounded-2xl h-10 px-4 hover:bg-red-700 focus:outline-none">
                Decline
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AdminCard;
