import { useState, useEffect } from "react";
import { Auth } from "aws-amplify";
import { useRouter } from "next/router";
import { withAuthenticator, AmplifySignOut } from "@aws-amplify/ui-react";

import Link from "next/link";

import Button from "react-bootstrap/Button";
import Image from "react-bootstrap/Image";

import FormTemplate from "../../src/components/Form";
import Layout from "../../src/components/Layout";

const Login = () => {
  const [user, setUser] = useState(null);
  useEffect(() => {
    // Acessa a sessão do usuário no cliente
    Auth.currentAuthenticatedUser()
      .then((user) => {
        console.log("User: ", user);
        setUser(user);
      })
      .catch((err) => setUser(null));
  }, []);

  if (!user) return null;

  return (
    <>
      <div>
        {user && (
          <>
            <h1 className="title">Seja bem vindo</h1>
            <Image
              src="/images/profile.png" // Route of the image file
              height={144} // Desired size with correct aspect ratio
              width={144} // Desired size with correct aspect ratio
              roundedCircle
              alt="coin poker"
              className="flame"
            />
            <p className="description">{user.username}</p>
            <AmplifySignOut />
          </>
        )}
      </div>
      {/* <h1 className="title">Acesso</h1>
      <p className="description">entre com seus dados</p>

      <FormTemplate></FormTemplate> */}
    </>
  );
};

export default withAuthenticator(Login);
