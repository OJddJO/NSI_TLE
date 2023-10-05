class Satellite:
    """A Satellite is defined by its name, its mass (=2000 by default) and its speed (=0 by default)."""
    def __init__(self, name, mass = 2000, speed = 0) -> None:
        self.name, self.mass, self.speed = name, mass, speed

    def impulsion(self, force, time) -> None:
        """This method changes the speed of the satellite.
        force is the force applied to the satellite, time is the duration of the force."""
        self.speed = (self.speed + force * time / self.mass).__round__(3)

    def energy(self) -> float:
        """This method returns the kinetic energy of the satellite.
        The kinetic energy is defined by 1/2 * mass * speed**2."""
        return 1/2 * self.mass * self.speed**2
    
    def show_speed(self) -> float:
        """This method returns the speed of the satellite."""            
        return self.speed
    
    def show_energy(self) -> float:
        """This method returns the kinetic energy of the satellite.
        The kinetic energy is defined by 1/2 * mass * speed**2."""
        return self.energy().__round__(2)

if __name__ == "__main__":
    s1 = Satellite("Eutelsat W3", mass=4400, speed=10)
    s2 = Satellite("Ariane 5", mass=750, speed=80)
    print(s1.show_speed())
    s1.impulsion(100, 15)
    print(s1.show_speed())
    print(s1.show_energy())
    print(s2.show_energy())
    print(round(s2.speed, 2))
