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


const inputValue = document.querySelector('#guess').value;
console.log(inputValue);

axios.post('/check-word', {
	guess: inputValue
})
.then((res) => {
	console.log(res);
	console.log(res.data.guessed_words);
})
.catch((err) => {
	console.log(err);
});

// axios({
// 	method: 'post',
// 	url: '/check-word',
// 	data: {guess: inputValue}
// });

// const form = document.querySelector('form');
// form.addEventListener('submit', (e) => {
// 	e.preventDefault();
// 	let inputValue = document.querySelector('#guess').value;

// 	axios.post('/check-word', {
// 		guess: inputValue,
// 	})
// 	.then((res) => {
// 		console.log(res);
// 	})
// 	.catch((err) => {
// 		console.log(err);
// 	});
// });


// const input_type = document.getElementById("name");
// console.log(input_type);
// const getPlayerGuess =  (e) =>{
// e.prevent()
// console.log("i came here")

// try {
//    const response =  axios.post('http://127.0.0.1:5000/check-word', {
//       // Data to be sent to the server
//       name: input_type
//    });
//    console.log(response.data);
// } catch (error) {
//    console.error(error);
// }
// }


