async function getJoke(first, last) {
    let res = await axios.get(`http://api.icndb.com/jokes/random?firstName=${first}&lastName=${last}`);
    console.log(res);
}

getJoke("Butters", "Steele");