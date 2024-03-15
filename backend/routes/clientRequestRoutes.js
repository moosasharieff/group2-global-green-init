const express = require('express');
const {createClientRequest, getAllGrants, getAllClientRequest} = require('../controllers/userController')

const router = express.Router();

router.post('/user-requests', createClientRequest);
router.get('/getGrants', getAllGrants)
router.get('/admin-client-requests', getAllClientRequest)

module.exports = router;