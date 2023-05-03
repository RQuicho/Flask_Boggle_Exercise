const getPlayerGuess = async () => {
  const inputValue = $('input #guess').val();
  const res = await axios.post('http://127.0.0.1:5000/', {params: {guess: inputValue}});
  console.log(res);

}