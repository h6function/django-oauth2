import { NextRequest } from "next/server"
import { cookies } from "next/headers";

interface UserEmailResponseBody {
  id: number;
  email: string;
  error?: string;
}

interface UserNameResponseBody {
  id: number;
  // username: string;
  last_name: string;
  first_name: string;
  error?: string;
}

export default async function profile(request: NextRequest) {
  const cookieStore = await cookies();
  const accessToken = cookieStore.get("access_token")?.value;

  if (!accessToken) {
    return (
      <>
        <h1>Profile Page</h1>
        <p>No access token found. Please log in first.</p>
      </>
    );
  }

  const userEmailResponse = await fetch(
    "http://app:8000/user/email/",
    {
      method: "GET",
      headers: {
        "Authorization": "Bearer " + (accessToken),
      },
    },
  );
  const userEmailResponseBody: UserEmailResponseBody = await userEmailResponse.json();

  const userNameResponse = await fetch(
    "http://app:8000/user/name/",
    {
      method: "GET",
      headers: {
        "Authorization": "Bearer " + (accessToken),
      },
    },
  );
  const userNameResponseBody: UserNameResponseBody = await userNameResponse.json();

  return (
    <>
      <h1>Profile Page</h1>
      <div>
        <h2>User Name</h2>
        {userNameResponse.ok ? (
          <>
          <p>First Name: {userNameResponseBody.first_name}</p>
          <p>Last Name: {userNameResponseBody.last_name}</p>
          </>
        ) : (
          <p>Failed to fetch profile: {userNameResponseBody.error || "Unknown error"}</p>
        )}
        <h2>User Email</h2>
        {userEmailResponse.ok ? (
          <p>Email: {userEmailResponseBody.email}</p>
        ) : (
          <p>Failed to fetch profile: {userEmailResponseBody.error || "Unknown error"}</p>
        )}
      </div>
    </>
  );
}
