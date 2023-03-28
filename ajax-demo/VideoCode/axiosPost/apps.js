// async function getUsers() {
//     const res = await axios.get('https://reqres.in/api/users');
//     console.log(res);
// }

// async function createUser() {
//     const res = await axios.post('https://reqres.in/api/users', {
//         username: "ButtersTheChicken",
//         email: "Butters@gmail.com",
//         age: 1
//     });
//     console.log(res);
// }

// getUsers();
// createUser();

async function getUsers(token) {
  const res = await axios.get(
    `https://hack-or-snooze-v3.herokuapp.com/users?skip=0&limit=10`, { params: { token } }
    );
    console.log(res);
}

async function signup(username, password, name) {
    const res = await axios.post(
      "https://hack-or-snooze-v3.herokuapp.com/signup",
      { user: { name, username, password } }
    );
  console.log(res);
}

async function login(username, password) {
  const res = await axios.post(
    "https://hack-or-snooze-v3.herokuapp.com/login",
    { user: { username, password } }
  );
  console.log(res);
  return res.data.token;
}
async function getUsersWithAuth() {
  const token = await login('Magikarp2.0', '123jlsajd');
  getUsers(token);
}

async function createStory() {
  const token = await login("Magikarp2.0", "123jlsajd");
    const newStory = {
      token,
      story: {
        author: "Egg",
        title: "Life in a bowl",
        url: "https://ellewhite.dev",
      },
    };
  const res = await axios.post(
    "https://hack-or-snooze-v3.herokuapp.com/stories", newStory
  );  
  console.log(res);
}

createStory();