import React, { Component } from 'react';
import injectTapEventPlugin from 'react-tap-event-plugin';
import SubmissionForm from './submission_form/containers/SubmissionForm';
import LoginScreen from './login/Loginscreen'
import './App.css';
// injectTapEventPlugin();
class App extends Component {
    constructor(props){
      super(props);
      this.state={
        loginPage:[],
        SubmissionForm:[]
      }
    }
    componentWillMount(){
      var loginPage =[];
      loginPage.push(<LoginScreen appContext={this}/>);
      this.setState({
                    loginPage:loginPage
                      })
      var form =[];
      form.push(<SubmissionForm appContext={this} />);
      this.setState({
                  form: form
      }); 
    }
    render() {
      return (
        <div className="App">
          {this.state.loginPage}
          {this.state.SubmissionForm}
        </div>
      );
    }
  }
  
  export default App;