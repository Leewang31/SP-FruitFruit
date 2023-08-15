const express = require('express');
const app = express();
const cors = require('cors'); // 추가
const path = require('path');

app.use(cors());
app.use('/', express.static(path.join(__dirname)));

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});