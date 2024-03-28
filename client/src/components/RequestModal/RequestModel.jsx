import { useEffect, useState } from "react";
import axios from "axios";

function RequestModel({ isOpen, onClose }) {
  const [userRequests, setUserRequests] = useState([]);
  const [grantMessage, setGrantMessage] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      const API_BASE_URL = `${process.env.REACT_APP_API_BASE_URL}api/get-user-requests`;
      try {
        const response = await axios.get(API_BASE_URL, {
          params: { email: "bishtshyam136@gmail.com" },
        });
        setUserRequests(response.data);
        
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    if (isOpen) {
      fetchData();
    }
  }, [isOpen]);

  if (!isOpen) {
    return null;
  }

  return (
    <div className="fixed inset-0 z-50 flex items-baseline justify-end overflow-auto bg-black bg-opacity-50">
      <div className="relative bg-white rounded-lg w-auto p-6 top-28 right-60">
        <button
          className="absolute top-0 right-0 m-2 text-gray-500 hover:text-gray-900"
          onClick={onClose}
        >
          &#x2715;
        </button>
        <div className="p-4 max-h-80 overflow-y-auto">
          <ul>
            {userRequests.map((request, index) => (
              <li
                className="w-full rounded-lg border border-slate-500 p-4 m-2 cursor-pointer hover:bg-slate-500"
                key={index}
              >
                {request.granterName} - {request.description} - {request.grantStatus === true ? "Approved" : "'wait for the confirmation'"}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default RequestModel;
