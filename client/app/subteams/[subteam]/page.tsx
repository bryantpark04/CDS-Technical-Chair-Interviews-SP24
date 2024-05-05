"use client"

import { usePathname, useSearchParams } from 'next/navigation'
import { useEffect } from 'react'
import { useParams } from 'next/navigation'

export default function NavigationEvents() {
    const params = useParams<{ subteam: string }>()

    return (
        <h1>
            {params.subteam} Subteam
        </h1>
    )
}