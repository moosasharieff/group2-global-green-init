const express = require('express');
const {createClientRequest, getAllGrants, getAllClientRequest} = require('../controllers/userController')

const router = express.Router();

/**
 * Route to create a new client request.
 * @name POST /api/user-requests
 * @function
 * @memberof module:routes/clientRequestRoutes
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Next middleware function.
 */
router.post('/user-requests', createClientRequest);

/**
 * Route to get all grants.
 * @name GET /api/getGrants
 * @function
 * @memberof module:routes/clientRequestRoutes
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Next middleware function.
 */
router.get('/getGrants', getAllGrants)

/**
 * Route to get all grants.
 * @name GET /api/getGrants
 * @function
 * @memberof module:routes/clientRequestRoutes
 * @param {Object} req - Express request object.
 * @param {Object} res - Express response object.
 * @param {Function} next - Next middleware function.
 */
router.get('/admin-client-requests', getAllClientRequest)

module.exports = router;