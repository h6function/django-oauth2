import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  const searchParams = request.nextUrl.searchParams;
  const code = searchParams.get("code");

  if (!code) {
    return NextResponse.json({ error: "No code provided" }, { status: 400 });
  }

  const formData = new FormData();
  formData.append("grant_type", "authorization_code");
  formData.append("code", code);
  formData.append("redirect_uri", "http://localhost:3000/oauth/callback");
  formData.append("client_id", "foobar");

  try {
    const tokenResponse = await fetch("http://app:8000/oauth/token/", {
      method: "POST",
      headers: {
        "Authorization": "Basic " + btoa("foobar:barbaz"),
      },
      body: formData,
    }).then((res) => res.json());

    const cookieStore = await cookies();
    cookieStore.set("access_token", tokenResponse.access_token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === "production",
      path: "/",
    });

    return NextResponse.redirect(new URL("/", request.url));

  } catch (error) {
    console.error("Token exchange failed:", error);
    return NextResponse.json({ error: "Authentication failed" }, { status: 500 });
  }
}