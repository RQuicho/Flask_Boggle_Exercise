// const getPlayerGuess =  (e) => {
//   e.preventDefault();
//   let inputValue = $('#guess').val();
//   console.log(inputValue);

//   const res =  axios.post('http://localhost:5000/check-word',{inputValue}).then((resp)=>{
//     console.log(resp);
//     console.log(res);


//   });


// }

// const input_type = document.getElementById("name");
// // const passwordInput = document.getElementById("password");
// console.log(input_type);
// const btn = document.getElementById("submit");

// btn.addEventListener("click", () => {
//   const inputype = input_type.value;
//   // const password = passwordInput.value;

//   axios.post("http://localhost:5000/check-word", {
//     inputype: inputype,
//       // password: password
//     })
//     .then((response) => {
//       console.log(response);
//     });
// });

const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
	e.preventDefault();
	let inputValue = document.querySelector('#guess').value;

	axios.post('/', {
		guess: inputValue,
	})
	.then((res) => {
		console.log(res);
	})
	.catch((err) => {
		console.log(err);
	});
});


