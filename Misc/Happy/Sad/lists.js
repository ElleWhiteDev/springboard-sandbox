const newTodo = document.createElement('li');
const boldText = document.createElement('b');
const ul = document.querySelector('ul');
boldText.textContent = "DONT FORGET TTO LOCK THE COOP!";
newTodo.classList = "todo";
newTodo.append(boldText);
ul.append(newTodo);

const secondTodo = document.createElement('li');
secondTodo.textContent = "Order more la croix";
secondTodo.className = "todo"

ul.append(newTodo, secondTodo);  

const thirdTodo = document.createElement('li');
thirdTodo.textContent = "Feed Cats";
ul.prepend(thirdTodo);

const newImg = document.createElement('img');
newImg.classList.add('thumbnail');
newImg.setAttribute('src', 'https://images.unsplash.com/photo-1517436073-3b3b1f3e8d0c?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=3b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b&auto=format&fit=crop&w=1350&q=80');

document.body.prepend(newImg);  

// const removeMe = document.querySelector('#remove-me');
// ul.removeChild(removeMe);

const removeMe = document.querySelector("#remove-me");
removeMe.remove();

const h1 = document.querySelector('h1');
h1.remove();

