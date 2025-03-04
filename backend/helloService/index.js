  GNU nano 7.2                                                           index.js                                                                    const express = require('express');
require('dotenv').config();
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.send({ msg: 'Hello World' });
});

app.get('/health', (req, res) => {
    res.send({ status: 'OK' });
});

app.listen(PORT, () => {
    console.log(`🚀 Server is running on port ${PORT}`);
});
