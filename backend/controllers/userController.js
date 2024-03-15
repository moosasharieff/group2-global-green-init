const ClientRequest = require('../models/ClientRequest');
const GrantsAll = require('../models/GrantSchema')
const AdminGrantRequests = require('../models/GrantSchema')

const createClientRequest = async (req, res) => {
  const { granterName, username, email, description, requestedAmount } = req.body;

  try {
    const newClientRequest = new ClientRequest({
      granterName,
      username,
      email,
      description,
      requestedAmount,
    });

    const savedClientRequest = await newClientRequest.save();

    res.status(201).json(savedClientRequest);
  } catch (error) {
    console.error('Error creating user request:', error.message);
    res.status(500).json({ error: 'Internal Server Error' });
  }
};


const getAllGrants = async(req, res) => {
  const allData = await GrantsAll.find();
  res.send(allData);
}

const getAllClientRequest = async(req, res) => {
  const allData = await ClientRequest.find();
  res.send(allData);
}

module.exports = { createClientRequest, getAllGrants, getAllClientRequest } 