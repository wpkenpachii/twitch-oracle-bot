const axios = require('axios')
const dotenv = require('dotenv')
dotenv.config()
const { ANSWER_URL_PROD, ANSWER_URL_DEV } = process.env;
const base_url = 'http://oracle:5000' // ANSWER_URL_PROD ? ANSWER_URL_PROD : ANSWER_URL_DEV

module.exports = {
    answer: async function(question) {
        try {
            const { data } = await axios.post(`${base_url}/query`, { question })
            return data;
        } catch (error) {
            console.log(error)
        }
    }
}