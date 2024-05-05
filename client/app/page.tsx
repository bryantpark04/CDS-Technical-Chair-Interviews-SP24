import Image from "next/image";
import Logo from "cds_logo.png"
// import styles from "client/app/main.css"


export default function Page() {
  return (
    <div className="content-center">
      <Image
        src="/cds_logo.png"
        width={500}
        height={500}
        alt="Picture of the author"
      />
      <h1>
        Cornell Data Science
      </h1>
    </div>

  )
}
