const character = document.getElementById('character');
const block = document.getElementById('block');
let gameStarted = false;

const jump = (function () {
	let checkDead;

	return function () {
		if (character.classList != "animate-jump") {
			character.classList.add("animate-jump");
		}
		setTimeout(function () {
			character.classList.remove("animate-jump");
		}, 500);

		if (!gameStarted) {
            gameStarted = true;

            resetBlockAnimation();

            block.classList.add("animate-block");

			checkDead = setInterval(function () {
				let characterTop = parseInt(
					window.getComputedStyle(character).getPropertyValue("top")
				);
				let blockLeft = parseInt(
					window.getComputedStyle(block).getPropertyValue("left")
				);
				if (blockLeft < 20 && blockLeft > 0 && characterTop >= 130) {
					block.style.animation = "none";
					block.style.display = "none";
                    alert("You Lose!");
                    location.reload();
				}
			}, 10);
		}
	};
})();

function resetBlockAnimation() {
    block.style.animation = 'none'

    setTimeout(function () {
        block.style.animation = 'block .6s linear';
    }, Math.random() * 400 + 100);
}

block.addEventListener('animationend', resetBlockAnimation);

document.addEventListener("keydown", jump);
document.addEventListener("click", jump);
