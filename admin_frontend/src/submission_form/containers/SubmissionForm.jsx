import React, {Component} from 'react';  

/* Import Components */
import Input from '../components/Input'; 
import Select from '../components/Select';
import Button from '../components/Button'

class SubmissionForm extends Component {  
  constructor(props) {
    super(props);

    this.state = {
      newRabbit: {
        name: '',
        breed: '',
        gender: '',
        size: ''

      },

      genderOptions: ['Male', 'Female'],
      sizeOptions: ['Large', 'Medium', 'Small']

    }
    this.handleFullName = this.handleFullName.bind(this);
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
    this.handleClearForm = this.handleClearForm.bind(this);
    this.handleInput = this.handleInput.bind(this);
  }

  /* This lifecycle hook gets executed when the component mounts */
  
  handleFullName(e) {
   let value = e.target.value;
   this.setState( prevState => ({ newRabbit : 
        {...prevState.newRabbit, name: value
        }
      }), () => console.log(this.state.newRabbit))
  }

  handleInput(e) {
       let value = e.target.value;
       let name = e.target.name;
   this.setState( prevState => ({ newRabbit : 
        {...prevState.newRabbit, [name]: value
        }
      }), () => console.log(this.state.newRabbit))
  }

  handleFormSubmit(e) {
    e.preventDefault();
    let rabbitData = this.state.newRabbit;

    fetch('http://localhost:3210/data',{
        method: "POST",
        body: JSON.stringify(rabbitData),
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      }).then(response => {
        response.json().then(data =>{
          console.log("Successful" + data);
        })
    })
  }   

  handleClearForm(e) {
  
      e.preventDefault();
      this.setState({ 
        newRabbit: {
          name: '',
          breed: '',
          gender: '',
          size: ''
        },
      })
  }

  render() {
    return (
    
        <form className="container-fluid" onSubmit={this.handleFormSubmit}>
       
            <Input inputType={'text'}
                   title= {'Full Name'} 
                   name= {'name'}
                   value={this.state.newRabbit.name} 
                   placeholder = {'Enter the name'}
                   handleChange = {this.handleInput}
                   
                   /> {/* Name of the Rabbit */}
        
          <Input inputType={'text'} 
                name={'breed'}
                 title= {'Breed'} 
                 value={this.state.newRabbit.breed} 
                placeholder = {'Enter the Breed'}
                 handleChange={this.handleInput} /> {/* Breed */} 


          <Select title={'Gender'}
                  name={'gender'}
                  options = {this.state.genderOptions} 
                  value = {this.state.newRabbit.gender}
                  placeholder = {'Select Gender'}
                  handleChange = {this.handleInput}
                  /> {/*Gender*/}

          <Select title={'Size'}
                  name={'size'}
                  options = {this.state.sizeOptions} 
                  value = {this.state.newRabbit.size}
                  placeholder = {'Select Size'}
                  handleChange = {this.handleInput}
                  /> {/*Size*/}

          <Button 
              action = {this.handleFormSubmit}
              type = {'primary'} 
              title = {'Submit'} 
            style={buttonStyle}
          /> { /*Submit */ }
          
          <Button 
            action = {this.handleClearForm}
            type = {'secondary'}
            title = {'Clear'}
            style={buttonStyle}
          /> {/* Clear the form */}
          
        </form>
  
  );
  }
}

const buttonStyle = {
  margin : '10px 10px 10px 10px'
}

export default SubmissionForm;