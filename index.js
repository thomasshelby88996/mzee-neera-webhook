// index.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = process.env.PORT || 3000;

app.use(bodyParser.json());

app.post('/webhook', (req, res) => {
    const agent = req.body.queryResult;
    const intent = agent.intent.displayName;
    let responseText = "";

    switch (intent) {
        case 'Welcome Intent':
            responseText = "Welcome to Mzee Neera 2026 bot 🇺🇬! Reply with:\n1️⃣ Manifesto\n2️⃣ Achievements\n3️⃣ Projects\n4️⃣ How to Apply";
            break;
        case 'Manifesto':
            responseText = "Here is our 2026 Manifesto:\n- Peace\n- Economic Empowerment\n- Youth & Women Initiatives\n🇺🇬 'Steady Progress, Steady Leadership'";
            break;
        case 'Achievements':
            responseText = "Past achievements include:\n- Universal Primary Education\n- Improved road infrastructure\n- Oil & Gas development";
            break;
        case 'Projects':
            responseText = "Ongoing projects include:\n1. Operation Wealth Creation\n2. Parish Development Model\n3. Emyooga Program";
            break;
        case 'Apply':
            responseText = "To benefit, visit: https://pdm.go.ug or contact your local government office.";
            break;
        default:
            responseText = "Sorry, I didn’t understand that. Please choose 1, 2, 3 or 4.";
    }

    res.json({ fulfillmentText: responseText });
});

app.listen(port, () => {
    console.log(`Webhook running on port ${port}`);
});
