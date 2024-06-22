export const buildings = [
    'Учебный корпус №2', //0
    'Учебный корпус №3', //1
    'Учебный корпус №6', //2
    'Учебный корпус №7', //3
    'Административный корпус', //4
    'Химический корпус', //5
    'Учебный корпус №1', //6
    'Актовый зал', //7
    'Библиотека', //8
    'Столовая' //9
]

export class RouteKey {
    source: string;
    destination: string;

    constructor(source: string, destination: string) {
        this.source = source;
        this.destination = destination;
    }

    isEqual(other: RouteKey): boolean {
        return (
            (this.source === other.source && this.destination === other.destination) ||
            (this.source === other.destination && this.destination === other.source)
        );
    }

    toString(): string {
        return `${this.source}-${this.destination}`;
    }
}

export class CustomMap<K extends RouteKey, V> extends Map<K, V> {
    get(key: K): V | undefined {
        for (const k of this.keys()) {
            if (k.isEqual(key)) {
                return super.get(k);
            }
        }
        return undefined;
    }
}


export const routesWithFilenames: CustomMap<RouteKey, string> = new CustomMap<RouteKey, string>([
    [new RouteKey(buildings[0], buildings[4]), "0-4.glb"],
    [new RouteKey(buildings[0], buildings[1]), "0-1.glb"],
    [new RouteKey(buildings[2], buildings[4]), "2-4.glb"],
    [new RouteKey(buildings[0], buildings[8]), "0-8.glb"],
    [new RouteKey(buildings[1], buildings[4]), "1-4.glb"],
    [new RouteKey(buildings[3], buildings[4]), "3-4.glb"],
    [new RouteKey(buildings[0], buildings[3]), "0-3.glb"],
    [new RouteKey(buildings[4], buildings[9]), "4-9.glb"],
    [new RouteKey(buildings[0], buildings[2]), "0-2.glb"],
    [new RouteKey(buildings[2], buildings[3]), "2-3.glb"],
    [new RouteKey(buildings[1], buildings[2]), "1-2.glb"],
    [new RouteKey(buildings[2], buildings[9]), "2-9.glb"],
    [new RouteKey(buildings[3], buildings[9]), "3-9.glb"],
    [new RouteKey(buildings[7], buildings[3]), "7-3.glb"],
    [new RouteKey(buildings[1], buildings[9]), "1-9.glb"],
]);

