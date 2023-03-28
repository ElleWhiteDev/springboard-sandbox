// async function getData() {
//     const response = await axios.get('https://swapi.dev/api/planets/');
//     const { next, results } = response.data;
    
//     for (let planet of results) {
//         console.log(planet.name);
//     }
   
//     const responseTwo = await axios.get(next);
//     const resultsTwo = responseTwo.data.results;
    
//     for (let planet of resultsTwo) {
//       console.log(planet.name);
//     }
// }

// getData();
// console.log('I happen after getData()');

async function getLaunches() {
    const res = await axios.get('https://api.spacejhxdata.com/v3/launches/upcoming');
    renderLaunches(res.data);   
}


function renderLaunches(launches) {
    const ul = document.querySelector("#launches");
    for (let launch of launches) {
       ul.append(makeLaunchLI(launch));
    }
}

function makeLaunchLI(launch) {
    const newLI = document.createElement('LI');
    const mission = document.createElement('B');
    newLI.append(mission)
    mission.innerText = launch.mission_name;
    newLI.innerHTML += ` - ${launch.rocket.rocket_name}`
    return newLI;
}

const btn = document.querySelector('#getLaunches');
btn.addEventListener('click', getLaunches);