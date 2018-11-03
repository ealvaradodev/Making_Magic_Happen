import React, { Component } from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';

import Login from './Login';

const style = {
  margin: 15,
};

class Loginscreen extends Component {
  constructor(props){
    super(props);
    var loginButtons=[];
    this.state={
      username:'',
      password:'',
      loginscreen:[],
      loginmessage:'',
      loginButtons:loginButtons,
      isLogin:true
    }
  }
  componentWillMount(){
    var loginscreen=[];
    loginscreen.push(<Login parentContext={this} appContext={this.props.appContext}/>);
    this.setState({
                  loginscreen:loginscreen,
                    })
  }
  handleClick(event,userRole){
    console.log("event",userRole);
    var loginmessage;
    if(this.state.isLogin){
      let loginscreen=[];
    //   loginscreen.push(<Register parentContext={this} appContext={this.props.appContext} role={userRole}/>);
      loginmessage = "Already registered.Go to Login";
      let loginButtons=[];
      loginButtons.push(
        <div key="login-button">
        <MuiThemeProvider>
          <div>
             <RaisedButton label={"Login"} primary={true} style={style} onClick={(event) => this.handleClick(event,userRole)}/>
         </div>
         </MuiThemeProvider>
        </div>
      )
      this.setState({
                     loginscreen:loginscreen,
                     loginmessage:loginmessage,
                     loginButtons:loginButtons,
                     isLogin:false
                   })
    }
    else{
      let loginscreen=[],loginButtons=[];
      loginButtons.push(
        <div>
        <MuiThemeProvider>
          <div>
             <RaisedButton label={"Register as user"} primary={true} style={style} onClick={(event) => this.handleClick(event,'user')}/>
         </div>
         </MuiThemeProvider>
         <MuiThemeProvider>
         <div>
            <RaisedButton label={"Register as admin"} primary={true} style={style} onClick={(event) => this.handleClick(event,'admin')}/>
        </div>
        </MuiThemeProvider>
        </div>
      )
      loginscreen.push(<Login parentContext={this} appContext={this.props.appContext} role={userRole}/>);
      loginmessage = "Not Registered yet.Go to registration";
      this.setState({
                     loginscreen:loginscreen,
                     loginmessage:loginmessage,
                     loginButtons:loginButtons,
                     isLogin:true
                   })
    }
  }
  render() {
    return (
      <div className="loginscreen" key="loginscreen">
        {this.state.loginscreen}
        <div>
          {this.state.loginmessage}
          {this.state.loginButtons}
        </div>
      </div>
    );
  }
}


export default Loginscreen;
