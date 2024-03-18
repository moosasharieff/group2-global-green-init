import { useState, useEffect } from 'react';
import Navbar from '../../components/navbar/Navbar';
import AdminCard from '../../components/Card/AdminCard';
import axios from 'axios'

const AdminPage = () => {
  const [clientRequest, setClientRequest] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      const api_url = `${process.env.REACT_APP_API_BASE_URL}api/admin-client-requests`;

      console.log(api_url)
      try {
        const response = await axios.get(api_url);
        setClientRequest(response.data);
        console.log(response)
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, []);
  return (
    <div>
      <Navbar />
      <div className="justify-center items-center bg-slate-700 top-50">
        {clientRequest.map((requests) => (
          <AdminCard
            key={requests._id}
            email={requests.email}
            username={requests.username}
            description={requests.description}
            requestedAmount={requests.requestedAmount}
          />
        ))}
      </div>
    </div>
  );
}

export default AdminPage;
