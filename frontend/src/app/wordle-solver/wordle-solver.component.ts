import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';


@Component({
  selector: 'app-wordle-solver',
  standalone: true,
  imports: [],
  templateUrl: './wordle-solver.component.html',
  styleUrl: './wordle-solver.component.css'
})
export class WordleSolverComponent {
  
  constructor(public route: Router){}
}
