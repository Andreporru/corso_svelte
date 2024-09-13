<script lang="ts">
	let display = '';
	let operand1: number | null = null;
	let operand2: number | null = null;
	let operator: string | null = null;
	let result: number | null = null;

	const appendNumber = (number: string) => {
		display += number;
	};

	const setOperator = (op: string) => {
		if (display) {
			operand1 = parseFloat(display);
			display = '';
			operator = op;
		}
	};

	const calculate = () => {
		if (operand1 !== null && operator && display) {
			operand2 = parseFloat(display);
			switch (operator) {
				case '+':
					result = operand1 + operand2;
					break;
				case '-':
					result = operand1 - operand2;
					break;
				case '*':
					result = operand1 * operand2;
					break;
				case '/':
					result = operand1 / operand2;
					break;
				default:
					result = null;
					break;
			}
			display = result !== null ? result.toString() : '';
			operand1 = result;
			operand2 = null;
			operator = null;
		}
	};

	const clear = () => {
		display = '';
		operand1 = null;
		operand2 = null;
		operator = null;
		result = null;
	};
</script>

<div class="calculator">
	<div class="display">
		{display}
	</div>
	<div class="buttons">
		<button onclick={() => appendNumber('7')}>7</button>
		<button onclick={() => appendNumber('8')}>8</button>
		<button onclick={() => appendNumber('9')}>9</button>
		<button onclick={() => setOperator('/')}>/</button>

		<button onclick={() => appendNumber('4')}>4</button>
		<button onclick={() => appendNumber('5')}>5</button>
		<button onclick={() => appendNumber('6')}>6</button>
		<button onclick={() => setOperator('*')}>*</button>

		<button onclick={() => appendNumber('1')}>1</button>
		<button onclick={() => appendNumber('2')}>2</button>
		<button onclick={() => appendNumber('3')}>3</button>
		<button onclick={() => setOperator('-')}>-</button>

		<button onclick={() => appendNumber('0')}>0</button>
		<button onclick={() => appendNumber('.')}>.</button>
		<button onclick={calculate}>=</button>
		<button onclick={() => setOperator('+')}>+</button>

		<button class="clear" onclick={clear}>C</button>
	</div>
</div>

<style>
	.calculator {
		width: 400px;
		margin: 50px auto;
		background: #fff;
		padding: 20px;
		border-radius: 10px;
		box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
		font-family: Arial, sans-serif;
	}

	.display {
		font-size: 2em;
		background: #f4f4f4;
		padding: 20px;
		border-radius: 5px;
		text-align: right;
		margin-bottom: 10px;
		border: 1px solid #ccc;
	}

	.buttons {
		display: grid;
		grid-template-columns: repeat(4, 1fr);
		gap: 10px;
	}

	button {
		background-color: blueviolet;
		color: white;
		border: none;
		padding: 20px;
		font-size: 1.5em;
		border-radius: 5px;
		cursor: pointer;
		transition: background-color 0.3s;
	}

	button:hover {
		background-color: rgb(78, 0, 78);
	}

	.clear {
		grid-column: span 4;
		background-color: #dc3545;
	}

	.clear:hover {
		background-color: #c82333;
	}
</style>
