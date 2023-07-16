const tmi = require('tmi.js');
const { answer } = require('./answer.js')
const dotenv = require('dotenv')
dotenv.config()
const {
    WPKENPACHII_OAUTH_TOKEN,
    SIRZARAKIKENPACHI_OAUTH_TOKEN
} = process.env;
let ligado = true;
const client = new tmi.Client({
    options: { debug: false },
	identity: {
        username: 'nany',
		password: WPKENPACHII_OAUTH_TOKEN,
	},
    channels: [ 'sirzarakikenpachi' ],
});

client.connect().then(() => {
    console.log('Connecting...')
});

client.on('message', (channel, tags, message, self) => {
	// Ignore echoed messages.
	if(self) return;

    // if (tags.username.match(/[sirzarakikenpachi|jorg1tos]/gmi) && message.match(/\!oraculo desligar/gmi)) {
    //     if (ligado) {
    //         client.say(channel, `Ok... desligannndo! Até mais pessoal!`)
    //         ligado = false
    //     }
    //     return
    // } else if (tags.username.match(/[sirzarakikenpachi|jorg1tos]/gmi) && message.match(/\!oraculo ligar/gmi)) {
    //     if (!ligado) {
    //         client.say(channel, `Aoooba! To de volta nesse carai!`)
    //         ligado = true
    //     }
    //     return
    // }

    // if (message.match(/\!oraculo [desligar|ligar]/gmi) || !ligado) {
    //     return
    // }

    if (!message.match(/\!oraculo/gmi)) return

    const payload = message.replace(/\!oraculo/gmi, '')
    answer(payload).then( response => {
        client.say(channel, `@${tags.username}, ${response}`)
    })
});