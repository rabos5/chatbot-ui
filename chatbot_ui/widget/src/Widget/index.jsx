import { persistor, store } from "../store";
import PropTypes from "prop-types";
import { Provider } from "react-redux";
import { PersistGate } from "redux-persist/integration/react";
import "./index.css";
import { WidgetLayout } from "./WidgetLayout";

export const Widget = (props) => {
  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <WidgetLayout {...props} />
      </PersistGate>
    </Provider>
  );
};

Widget.prototype = {
  rasaServerUrl: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  initialPayload: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  userId: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  metadata: PropTypes.oneOfType([PropTypes.object, PropTypes.element]),
  botAvatar: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  widgetColor: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  botTitle: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  botSubTitle: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  textColor: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  userMsgBackgroundColor: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.element,
  ]),
  botMsgBackgroundColor: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.element,
  ]),
  botMsgColor: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  botResponseDelay: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  userMsgColor: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
  chatHeaderTextColor: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.element,
  ]),
  buttonsCss: PropTypes.oneOfType([PropTypes.object, PropTypes.element]),
  errorMessages: PropTypes.oneOfType([PropTypes.array, PropTypes.element]),
  chatHeaderCss: PropTypes.oneOfType([PropTypes.object, PropTypes.element]),
  embedded: PropTypes.oneOfType([PropTypes.string, PropTypes.element]),
};

Widget.defaultProps = {
  rasaServerUrl: "http://localhost:5005/webhooks/rest/webhook",
  // senderId: "",
  userId: "chatbot_sandbox_user",
  initialPayload: "/greet",
  metadata: {},
  botTitle: "ChatBot Sandbox - Widget",
  // botSubTitle: "",
  enableBotAvatar: false,
  // botAvatar: "data:image/png;base64,",
  enableDropdownMenu: false,
  widgetColor: "#079543",
  textColor: "#ffffff",
  chatHeaderCss: {
    // enableBotAvatarBorder: true,
    textColor: "#ffffff",
    backgroundColor: "#079543",
  },
  chatHeaderTextColor: "#ffffff",
  botMsgBackgroundColor: "#f3f4f6",
  botMsgColor: "#4b5563",
  userMsgBackgroundColor: "#e1d7ff",
  userMsgColor: "#4c1d95",
  botResponseDelay: "",
  embedded: false,
  buttonsCss: {
    color: "#ffffff",
    backgroundColor: "#079543",
    borderColor: "#ffffff",
    borderWidth: "1x",
    borderRadius: "0px 20px 20px 0px",
    // hoverBackgroundColor: "#079543",
    // hoverColor: "#4b5563",
    // hoverborderWidth: "1px",
    enableHover: false,
  },
};
