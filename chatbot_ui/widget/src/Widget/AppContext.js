import { createContext } from "react";

const AppContext = createContext({
  rasaServerUrl: "",
  initialPayload: "",
  metadata: {},
  enableBotAvatar: false,
  enableDropdownMenu: false,
  botAvatar: "",
  widgetColor: "",
  botTitle: "",
  botSubTitle: "",
  userId: null,
  textColor: "",
  userMsgBackgroundColor: "",
  botMsgBackgroundColor: "",
  botMsgColor: "",
  userMsgColor: "",
  botResponseDelay: "",
  buttonsCss: {},
  chatHeaderCss: {},
  errorMessages: [],
  embedded:false
});

export default AppContext;
