// import Image from "next/image";
import Link from "next/link";

export default function Home() {
  const genAuthorizationUrl = (scopes: string[]) => {
    const authorizationParams = new URLSearchParams({
      response_type: "code",
      client_id: "foobar",
      redirect_uri: "http://localhost:3000/oauth/callback",
    });
    if (scopes.length > 0) {
      authorizationParams.set("scope", scopes.join(" "));
    }
    return `http://localhost:8000/oauth/authorize?${authorizationParams.toString()}`;
  };

  return (
    <div className={[
      // "bg-zinc-50",
      // "dark:bg-black",
      "flex",
      "font-sans",
      // "items-center",
      "justify-center",
      "min-h-screen",
    ].join(" ")}>
      <main className={[
        "flex",
        "flex-col",
        "w-full",
      ].join(" ")}>
        <h1>Root access</h1>
        <Link href={`${genAuthorizationUrl(["user.name"])}`}>Go to OAuth authorization with scopes: user.name</Link>
        <Link href={`${genAuthorizationUrl(["user.email", "user.name"])}`}>Go to OAuth authorization with scopes: user.email user.name</Link>
        <Link href="/profile">Go to Profile</Link>
      </main>
    </div>
  );
}
